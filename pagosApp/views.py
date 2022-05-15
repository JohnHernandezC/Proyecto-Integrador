from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
from paypalcheckoutsdk.orders import OrdersGetRequest, OrdersCaptureRequest
from .models import *
from publicacionesApp.models import *

import sys, json


def pago(request):
    curso = Post.objects.get(pk=2)
    data = json.loads(request.body)
    order_id = data['orderID']

    detalle = GetOrder().get_order(order_id)
    detalle_precio = float(detalle.result.purchase_units[0].amount.value)
    print(detalle_precio)

    if detalle_precio == curso.precio:
        trx = CaptureOrder().capture_order(order_id, debug=True)
        pedido = Compra(
            id= request.user.pk, 
            estado= trx.result.status, 
            codigo_estado= trx.status_code, 
            producto= Post.objects.get(pk=2),
            total_de_la_compra = trx.result.purchase_units[0].payments.captures[0].amount.value, 
            nombre_cliente= request.user.nombres, 
            apellido_cliente= request.user.apellidos, 
            correo_cliente= request.user.email, 
            direccion_cliente= trx.result.purchase_units[0].shipping.address.address_line_1)
        pedido.save()

        data = {
            "id": f"{trx.result.id}",
            "nombre_cliente": f"{trx.result.payer.name.given_name}",
            "mensaje": "pago realizado de manera correcta"
        }
        return JsonResponse(data)
    else:
        data = {
            "mensaje": "Lo sentimos, no pudimos realizar el pago =("
        }
        return JsonResponse(data)

class PayPalClient:
    def __init__(self):
        self.client_id = "Af6Xi9WXzy-aPWSKygyMggcqCk8aEzo-COV2FmnD_SYV0nxjeutJ-7azGumtFLxwb4JVlHN-RGuQIK-4"
        self.client_secret = "EOnGkDR_dLnRHsWIYxjR31ri6Ad52C9VGcZT4oAH1hB8gEfB7CiJVKGkJzm5ZdwjSsDkh0y_uPXu41aB"

        """Set up and return PayPal Python SDK environment with PayPal access credentials.
           This sample uses SandboxEnvironment. In production, use LiveEnvironment."""

        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)

        """ Returns PayPal HTTP client instance with environment that has access
            credentials context. Use this instance to invoke PayPal APIs, provided the
            credentials have access. """
        self.client = PayPalHttpClient(self.environment)

    def object_to_json(self, json_data):
        """
        Function to print all json data in an organized readable manner
        """
        result = {}
        if sys.version_info[0] < 3:
            itr = json_data.__dict__.iteritems()
        else:
            itr = json_data.__dict__.items()
        for key,value in itr:
            # Skip internal attributes.
            if key.startswith("__"):
                continue
            result[key] = self.array_to_json_array(value) if isinstance(value, list) else\
                        self.object_to_json(value) if not self.is_primittive(value) else\
                         value
        return result
    def array_to_json_array(self, json_array):
        result =[]
        if isinstance(json_array, list):
            for item in json_array:
                result.append(self.object_to_json(item) if  not self.is_primittive(item) \
                              else self.array_to_json_array(item) if isinstance(item, list) else item)
        return result

    def is_primittive(self, data):
        return isinstance(data, str) or isinstance(data, unicode) or isinstance(data, int)


## Obtener los detalles de la transacción
class GetOrder(PayPalClient):

  #2. Set up your server to receive a call from the client
  """You can use this function to retrieve an order by passing order ID as an argument"""   
  def get_order(self, order_id):
    """Method to get order"""
    request = OrdersGetRequest(order_id)
    #3. Call PayPal to get the transaction
    response = self.client.execute(request)
    return response
    #4. Save the transaction in your database. Implement logic to save transaction to your database for future reference.
    # print 'Status Code: ', response.status_code
    # print 'Status: ', response.result.status
    # print 'Order ID: ', response.result.id
    # print 'Intent: ', response.result.intent
    # print 'Links:'
    # for link in response.result.links:
    #   print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
    # print 'Gross Amount: {} {}'.format(response.result.purchase_units[0].amount.currency_code,
    #                    response.result.purchase_units[0].amount.value)

# """This driver function invokes the get_order function with
#    order ID to retrieve sample order details. """
# if __name__ == '__main__':
#   GetOrder().get_order('REPLACE-WITH-VALID-ORDER-ID')


class CaptureOrder(PayPalClient):

  #2. Set up your server to receive a call from the client
  """this sample function performs payment capture on the order.
  Approved order ID should be passed as an argument to this function"""

  def capture_order(self, order_id, debug=False):
    """Method to capture order using order_id"""
    request = OrdersCaptureRequest(order_id)
    #3. Call PayPal to capture an order
    response = self.client.execute(request)
    #4. Save the capture ID to your database. Implement logic to save capture to your database for future reference.
    if debug:
      print ('Status Code: ', response.status_code)
      print ('Status: ', response.result.status)
      print ('Order ID: ', response.result.id)
      print ('Links: ')
      for link in response.result.links:
        print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
      print ('Capture Ids: ')
      for purchase_unit in response.result.purchase_units:
        for capture in purchase_unit.payments.captures:
          print ('\t', capture.id)
      print ("Buyer:")
        # print "\tEmail Address: {}\n\tName: {}\n\tPhone Number: {}".format(response.result.payer.email_address,
        # response.result.payer.name.given_name + " " + response.result.payer.name.surname,
        # response.result.payer.phone.phone_number.national_number)
    return response
"""This driver function invokes the capture order function.
Replace Order ID value with the approved order ID. """
# if __name__ == "__main__":
#   order_id = 'REPLACE-WITH-APPORVED-ORDER-ID'
#   CaptureOrder().capture_order(order_id, debug=True)