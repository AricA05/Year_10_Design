//Step 1: Grab all the objects on the page I need for manipulation of the page

const login_form = document.querySelector("#login_form")

const login_nav = document.getElementById("login_nav")
const logout_nav = document.getElementById("logout_nav")
const learn_more_nav = document.getElementById("learn_more_nav")
const elements_nav = document.getElementById("elements_nav")



var users = ["user1", "user2", "user3"]
var pwords = ["pword1", "pword2", "pword3"]




login_form.addEventListener("submit",(e) => {
	console.log(e.bubble)
	e.preventDefault()


	//Step 1: 
	//Take form information
	console.log(login_form)
	user = login_form["user_name"].value
	password = login_form["user_password"].value
	console.log(user,password)

	//Option 1: Veify against a predefined list - for learning
	//WE ARE GOING TO AIM FOR THIS

	//Take input from the submitted form and check to if the username and password are valid

	//Step 2:
	//Create flad valid = false
	valid = false //BIG IDEA: Have a variable that validates a condidation I can act on later



	//Step 3:
	for (i = 0; i < users.length; i = i + 1) {

		if (users[i] === user) {

			if (pwords[i] === password) {
				valid = true //The user exists in the system
			}
		}
	}

	if (valid === true) {
		login_nav.style.display = "none"
		logout_nav.style.display = "block" //display the logout_nav button
		learn_more_nav.style.display = "block"
		elements_nav.style.display = "block"

	}
	else {
		  M.toast({html: 'I am a toast!'})
	}
	//Loop through users to check for user
		//if users[i] == user
			//if pwords[i] == pword
				//set valid to true

	//Step 4:
	//if valid is true then you are going to change the diplsay
	//if valid is false then tel

	//manually close modal
	const modal = document.querySelector('#login_modal'); 
	//M is the materialze tol box that I have access to since I loaded the resources 
	//Modal is the set tools inside M for modals 
	//getInstance is a special function that I pass the modal object to 
	//close()
	M.Modal.getInstance(modal).close();
	//clears the content in the modal
	login_form.reset()


});

logout_nav.addEventListener("click", (e) => {

	//changed display back to navbar button
	login_nav.style.display = "block"
	logout_nav.style.display = "none"
	learn_more_nav.style.display = "none"
	elements_nav.style.display = "none"

});






