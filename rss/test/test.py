import azure_rss, aws_status
response = {}
response['azure'] = azure_rss.read()
response['aws'] = aws_status.read()

print(response)

