import webbrowser
from urllib.parse import quote
import os

def img_gen(text):
    css="""
    body {
        font-family: Arial, sans-serif;
        text-align: center;
        margin: 0;
        padding: 0;
      }
      #imageContainer {
        margin-top: 20px;
      }
      #mainImage {
        width: 500px;
        display: none;
      }
      #loader {
        display: none;
      }
      #downloadButton {
        margin-top: 20px;
        padding: 10px 20px;
        font-size: 16px;
        background-color: #4caf50;
        color: white;
        border: none;
        cursor: pointer;
        display: none;
      }
      #downloadButton:hover {
        background-color: #45a049;
      }
    """
    js="""
    const mainImage = document.getElementById('mainImage');
              const loader = document.getElementById('loader');
              const downloadButton = document.getElementById('downloadButton');

              loader.style.display = 'block';
              mainImage.style.display = 'none';

              mainImage.onload = function() {
                  loader.style.display = 'none';
                  mainImage.style.display = 'block';
                  downloadButton.style.display = 'inline-block';
              };

              mainImage.onerror = function() {
                  loader.style.display = 'none';
                  imageContainer.innerText = 'Failed to load image';
              };

      //         downloadButton.onclick = function() {
      //     const link = document.createElement('a');
      //     link.href = mainImage.src;
      //     link.download = 'ai_generated_image.jpg';
      //     document.body.appendChild(link);
      //     link.click();
      //     document.body.removeChild(link);
      // };

      document.addEventListener('DOMContentLoaded', function() {
          const downloadButton = document.getElementById('downloadButton');
          const mainImage = document.getElementById('mainImage');

          downloadButton.addEventListener('click', function() {
              const imageUrl = mainImage.src;
              fetch(imageUrl)
                  .then(response => response.blob())
                  .then(blob => {
                      const downloadLink = document.createElement('a');
                      downloadLink.href = URL.createObjectURL(blob);
                      downloadLink.download = 'image.jpg';
                      document.body.appendChild(downloadLink);
                      downloadLink.click();
                      document.body.removeChild(downloadLink);
                  })
                  .catch(error => console.error('Error downloading image:', error));
          })}
        )
    """
    html=f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ai Image</title>
        <style>
        {css}
        </style>
    </head>
    <body>
        <h1>AI GEN IMAGE</h1>
        <div id="imageContainer" style="text-align: center">
        <img
            style="margin-left: auto; margin-right: auto"
            id="mainImage"
            src="https://pollinations.ai/prompt/{quote(text)}"
            alt=""
        />
        <div id="loader">Loading...</div>
        </div>
        <button id="downloadButton">Download Image</button>

    <script>
        {js}
    </script>
    </body>
    </html>
    """

    file_path="img/index.html"

    with open(file_path, "w") as f:
        f.write(html)

    url="file://"+os.path.realpath(file_path)

    webbrowser.open(url)