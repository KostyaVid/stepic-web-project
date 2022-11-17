def app(env, start_response):  
   body = '/n'.join(env['QUERY_STRING'].split('&')).encode('utf-8')
   headers = [('Content-type', 'text/plain; charset=utf-8')] 
   start_response('200 OK', headers)
   return  [body]