def app(env, start_response):  
   body = '/n'.join(env['QUERY_STRING'].split('&'))
   headers = [('Content-type', 'text/plain'),('Content-length',str(len(body)))] 
   start_response('200 OK', headers)
   return  body