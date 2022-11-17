def app(env, start_response):  
   body = [bytes(i + '\n', 'ascii') for i in env['QUERY_STRING'].split('&')]
   headers = [('Content-type', 'text/plain; charset=utf-8')] 
   start_response('200 OK', headers)
   return  body