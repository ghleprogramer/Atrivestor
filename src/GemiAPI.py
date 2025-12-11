from google import genai
import pathlib

def get_key():
	key = ""
	with open("data/api_key.txt", "r") as fkey:
		key = fkey.read()
	return key

def gemini_summary(fpath, prompt):
	api_key = get_key()
	if not api_key:
		raise IOError
	
	client = genai.Client(api_key=api_key)
	file_path = pathlib.Path(fpath)
	model = "gemini-2.5-flash"

	response = client.models.generate_content(
		model=model,
		contents=[
			genai.types.Part.from_bytes(
				data=file_path.read_bytes(),
				mime_type="application/pdf",
			),
			prompt,
		]
	)

	return response.text