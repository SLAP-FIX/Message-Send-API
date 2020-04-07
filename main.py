import sys
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException

if __name__ == "__main__":
    
    api_key = ""
    api_secret = ""
    
    params = dict()
    params['type'] = 'sms' 
    params['to'] = '' 
    params['from'] = '' 
    main_text = "내용을 입력하세요."
    params['text'] = main_text
    cool = Message(api_key, api_secret)
    response = cool.send(params)
    print("Success Count : %s" % response['success_count'])
    print("Error Count : %s" % response['error_count'])
    print("Group ID : %s" % response['group_id'])
sys.exit()
