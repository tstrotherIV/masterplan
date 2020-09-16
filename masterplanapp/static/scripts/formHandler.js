const saveButton = document.querySelectorAll(".save-and-next")


saveButton.forEach(function (btn) {
  let buttonId= btn.id.split('-')[1]
  btn.addEventListener('click', () => {console.log(buttonId)})
})

const postProjectData = (param) => {
  
  //fetch post to the appr route
  fetch(`${param}/`, {
    method: 'POST',
    body: JSON.stringify(data)
  })
}