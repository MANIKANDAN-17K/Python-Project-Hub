import asyncio as asyn

async def fetch_data():
	print ("Fetching data ...")
	await asyn.sleep(3)
	result = "Data fetched successfully!"
	return result
async def main():
	result = await fetch_data()
	print(result)
if __name__ == "__main__":
	asyn.run(main())
