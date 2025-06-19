// # Fase di preparazione
// Raccogliamo gli elementi di interesse dalla pagina
const mainSection = document.querySelector('main')
const nameField = document.querySelector('input')
const emojiElements = document.querySelectorAll('.emoji')
const generateButton = document.querySelector('#generate')

const storyTitle = document.querySelector('.story-title')
const storyText = document.querySelector('.story-text')
const homeButton = document.querySelector('#home')
const continueButton = document.querySelector('#continue')

// Preparo una variabile per la lista delle emoji scelte
const selectedEmojis = []

// Preparo una variabile per la lista di messaggi
const chatMessages = []

// Informazioni necessarie per chiamare GPT
const endpoint = 'https://api.openai.com/v1/chat/completions'

const API_KEY = 'METTI LA TUA API KEY QUI'


// Funzione che colora le emoji selezionate
function colorSelectedEmojis() {
  for (const element of emojiElements) {
    // Recupero l'emoji di ogni elemento
    const emoji = element.innerText

    // Se l'emoji è nella lista delle selezionate...
    if (selectedEmojis.includes(emoji)) {
      // Aggiungi la classe selected
      element.classList.add('selected')
    } else {
      // Rimuovi (se c'è la clase selected)
      element.classList.remove('selected')
    }
  }
}

// Funzione che chiede a GPT di creare una storia
async function createStory(prompt) {
  // Lo aggiungo alla lista dei messaggi
  chatMessages.push(prompt)

  // Mostro la schermata di caricamento
  mainSection.className = 'loading'

  // || SIAMO PRONTI A CHIAMARE GPT!!!!

  // Chiamiamo chatGPT
  const response = await fetch(endpoint, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${API_KEY}`
    },
    body: JSON.stringify({
      model: 'gpt-3.5-turbo',
      temperature: 0.7,
      messages: chatMessages
    })
  });

  // Elaboriamo la risposta
  const data = await response.json();

  // Recuperiamo la storia
  const story = JSON.parse(data.choices[0].message.content)

  // Mettiamo subito la risposta nella lista dei messaggi
  chatMessages.push({
    role: 'assistant',
    content: JSON.stringify(story)
  })

  // Inseriamo la storia all'interno della pagina
  storyTitle.innerText = story.title
  storyText.innerText = story.text

  // Mostra la schermata result
  mainSection.className = 'result'
}

// # Fase di gestione eventi
// Per ogni elemento degli elementi emoji...
for (const element of emojiElements) {
  // Stai attento se qualcuno clicca l'elemento
  element.addEventListener('click', function () {
    // Recupera l'emoji
    const clickedEmoji = element.innerText

    // ! Controllo se c'è già, non fare niente
    if (selectedEmojis.includes(clickedEmoji)) {
      console.warn(`Emoji ${clickedEmoji} già presente`)
      return
    }

    // Inseriscila nella lista delle selezionate
    selectedEmojis.push(clickedEmoji)


    // Se ci sono più di 3 emoji, togli "la più vecchia"
    if (selectedEmojis.length > 3) {
      console.warn('Ci sono troppe emoji, tolgo la prima')
      selectedEmojis.shift()
    }

    // Colora gli elementi le cui emoji sono in lista
    colorSelectedEmojis()

    console.log(selectedEmojis)
  })
}


// Al click del bottone "GENERA"
generateButton.addEventListener('click', async function () {
  // Recuperiamo il nome del protagonista
  const name = nameField.value

  // Controlle se manca qualcosa
  if (selectedEmojis.length < 3 || name.length < 2) {
    window.alert('Devi selezionare 3 emoji e inserire un nome')
    return
  }

  // Preparo il messaggio iniziale
  const prompt = {
    role: 'user',
    content: `Crea una storia a partire da queste emoji: ${selectedEmojis}. Il protagonista della storia si chiama ${name}. La storia deve essere breve e avere un titolo, anche questo molto breve. Le tue risposte sono solo in formato JSON come questo esempio: 
    
    {
      "title": "Incontro intergalattico",
      "text": "Durante un'esplorazione notturna, Alberto Angela s'imbatte in un'astronave aliena atterrata a Roma. Gli extraterrestri cercano aiuto contro un'orda di gatti robotici. Angela li aiuta e in cambio gli alieni gli regalano un'astronave.",
    }
    
    Assicurati che le chiavi del JSON siano "title" e "text", con virgolette.`
  }

  // Crea storia
  createStory(prompt)
})

// Al click sul bottone avanti
continueButton.addEventListener('click', function () {
  // Prepariamo un nuovo prompt
  const prompt = {
    role: 'user',
    content: 'Continua la storia da qui. Scrivi un breve paragrafo che prosegua la storia precedente. Le tue risposte sono solo in formato JSON con lo stesso formato delle tue risposte precedenti. Mantieni lo stesso valore per "title". Cambia solo il valore di "text"'
  }

  // Crea storia
  createStory(prompt)

})

// Al click sul bottone home
homeButton.addEventListener('click', function () {
  // Ricarica la pagina
  window.location.reload()
})