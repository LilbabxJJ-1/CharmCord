import aiohttp


async def charmAI(args, context):
    api_token = '...'

    # Set up the API base URL
    base_url = 'https://api.gitbook.com/v1'
    space_id = "zxDSJg6koIjslgO2E0IN"

    # Define the request body as a dictionary
    request_body = {
        "query": args,
        # Add other search parameters as needed
    }

    # Use aiohttp to make an asynchronous POST request
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{base_url}/spaces/{space_id}/search/ask',
                                json=request_body,
                                headers={'Authorization': f'Bearer {api_token}'}) as response:
            if response.status == 200:
                books_data = await response.json()
                try:
                    answer_text = books_data["answer"]["text"]
                    return answer_text
                except KeyError:
                    return "No Answer.. | Try again"
            else:
                return None
