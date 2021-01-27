//Step 1: Grab all the objects on the page I need for manipulation of the page

const login_form = document.querySelector("#login_form")

const login_nav = document.getElementById("login_nav")
const logout_nav = document.getElementById("logout_nav")
const learn_more_nav = document.getElementById("learn_more_nav")
const elements_nav = document.getElementById("elements_nav")

login_form.addEventListener("submit",(e) => {
	e.preventDefault()


	//Option 1: Veify against a predefined list - for learning
	//WE ARE GOING TO AIM FOR THIS


	//Option 2: authenticate using firebase or other 3rd party
	//




	logout_nav.style.display = "none"
	logout_nav.style.display = "block" //display the logout_nav button
	learn_more_nav.style.display = "block"
	elements_nav.style.display = "block"

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
	logout_nav.style.display = "block"
	logout_nav.style.display = "none"
	learn_more_nav.style.display = "none"
	elements_nav.style.display = "none"

});