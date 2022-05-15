

class PruebaMiddleware:
    
    def __init__(self,get_response):        
        self.get_response = get_response
    
    def __call__(self,request):
        response = self.get_response(request)
        #print(response.user)
        return response

    def process_view(self,request,view_func,view_args,view_kwargs):
        print (request.user)
        print("si")