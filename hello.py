def app(env, start_response):  
   headers = [('Content-type', 'text/plain')] 
   body = env['QUERY_STRING'].split('&')
   start_response('200 OK', headers)
   return  body