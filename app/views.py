from django.shortcuts import render
from .forms import PromptForm
from django.contrib.auth.forms import UserCreationForm
from project.settings import API_KEY

import openai
# openai.ape_key = ""
client = openai.OpenAI(api_key=API_KEY)


# Create your views here.
def home(request):
    response_text= None
    response_image = None

    if request.method == "POST":
        form= PromptForm(request.POST)
        #is_valid
        if form.is_valid():
            prompt = form.cleaned_data["prompt"]

            completion = client.chat.completions.create(
                model="gpt-4.1",
                messages=[
                    {"role": "developer", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )

            response_text = completion.choices[0].message.content

            # generation of images

            # image_result = client.images.generate(
            #     model="dall-e-3",
            #     prompt=prompt
            # )
            #
            # response_image = image_result.data[0].url

            image_result = client.images.generate(
                model="gpt-image-1",
                prompt=prompt
            )

            image_base64 = image_result.data[0].b64_json
            response_image = image_base64.b64decode(image_base64)




    else:
        form = PromptForm

    return render(request, "home.html", {
        "form":form,
        "response_text": response_text,
        "response_image": response_image
    })


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})