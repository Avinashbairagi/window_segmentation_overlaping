from simple_image_download import simple_image_download as simp

respons = simp.simple_image_download

keywords = ["inside windows","Home Windows"]

for kw in keywords:
    respons().download(kw,200)
