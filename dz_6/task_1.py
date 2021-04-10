import requests

response = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
logs = response.text

with open('nginx_logs.txt', 'w', encoding='utf-8') as f:
   f.write(logs)

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    def logs_parse(fl):
        remote_addr, _, _, _, _, request_type, requested_resource, *rest = fl.split()
        chunk = remote_addr, request_type.strip('"'), requested_resource
        return chunk
    
    logs_parsed = list(map(logs_parse, f))
    
    def logs_result(end, start=0):
        for i in logs_parsed[start:end]:
            print(i)
      
            
    logs_result(5)
    
  
    
   

    


