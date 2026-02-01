# Ollama + Colab

---

This setup lets you run **any LLM** inside **Google Colab**, using the **cloud GPU** provided by Colab.

## Features

* Run Ollama-powered LLMs directly in Colab
* Exposes a **web endpoint** to use the model like a chatbot
* Supports **inline chat** (non-web version)


## How to Use

1. Clone or download this repository to your local machine.

2. Open **Google Colab** and upload the provided `.ipynb` notebook file from the repository.

   * You can drag and drop the file into Colab, or
   * Use **File → Upload notebook** in Colab.

3. In Colab, make sure a **GPU runtime** is enabled:

   * Go to **Runtime → Change runtime type**
   * Select **GPU** as the hardware accelerator
     
4. follow note-book

> 💡 Tip: Keep the Colab session active while using the web endpoint, as the service stops when the session disconnects.
