<template>
  <div id="app">
    <div id="titles">
      <h1>ASISTENTE DE POSGRADOS</h1>
      <h2>DEPARTAMENTO DE INGENIERÍA DE SISTEMAS Y COMPUTACIÓN</h2>
    </div>  
    <div id="welcome">
      <br>Bienvenido, ¿en qué puedo ayudarle?</br>
    </div>
    <div id="wrapper">
      <div id="messages_container">
        <div class="message">
          <div id="end_div"></div>
          <div v-for="message in chat" :class="{ text_right: message.me, text_left: !message.me }">
            <div><strong>{{ message.me ? "Yo" : "Watson" }}</strong> {{ message.time }}</div>
            <p>{{ message.text }}</p>
          </div>
        </div>
      </div>
      <div id="footer">
        <div id="msg_input_wrapper">
          <input type="text" name="question" id="question" placeholder="Enviar mensaje" @keyup.enter="add_message">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const chat = []
const data = { chat }
export default {
  name: 'app',
  data () {
    return data
  },
  methods: {
    add_message () {
      const questionElement = document.getElementById('question')
      const question = questionElement.value
      const message = {}
      message.me = true
      message.text = question
      message.time = formatDate(new Date())
      this.chat.push(message)
      questionElement.value = ''
      this.$http.get('http://localhost:8000/watson/' + question).then((response) => {
        const answer = response.body.output.text[0] ? response.body.output.text[0] : 'Sé un poco más claro'
        const message = {}
        message.me = false
        message.text = answer
        message.time = formatDate(new Date())
        this.chat.push(message)
        questionElement.focus()
      })
    }
  }
}
function formatDate (date) {
  let hour = date.getHours() > 12 ? date.getHours() - 12 : date.getHours()
  hour = hour < 10 ? '0' + hour : hour
  const minute = date.getMinutes() < 10 ? '0' + date.getMinutes() : date.getMinutes()
  const ampm = date.getHours() > 12 ? 'PM' : 'AM'
  return hour + ':' + minute + ' ' + ampm
}
</script>

<style>
  html {
    height: 100%;
  }

  body {
    height: 100%;
    margin: 0;
  }

  #app {
    display: flex;
    flex-direction: column;
    flex-grow: 1;
    height: 100%;
  }
  
  #titles{
    text-align: center;
  }
  #welcome{
    text-align: right;
  }

  #wrapper {
    position: relative;
    display: flex;
    flex: 1;
    flex-direction: column;
    padding: 20px;
  }

  #messages_container {
    overflow-y: auto;
    position: relative;
    flex: 1;
    display: flex;
    flex-direction: column;
    outline: 0;
    padding: 10px;
  }

  #msg_input_wrapper {
    border: 2px solid rgba(160,160,162,.7);
    border-radius: .375rem;
    padding: 10px;
  }

  #question {
    width: 100%;
    border: 0;
  }

  #question:focus {
    outline: none;
  }

  #end_div {
    margin-top: auto;
  }

  #footer {
    order: 1;
    flex-shrink: 0;
    width: 100%;
  }

  .message {
    position: relative;
    flex: 1;
    display: flex;
    flex-direction: column;
    outline: 0;
  }

  .text_right {
    text-align: right;
  }

  .text_left {
    text-align: left;
  }
</style>
