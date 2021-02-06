   // Initialize Firebase
        var config = {
        apiKey: "AIzaSyAq7mI4o4Xi-eqVyV43WzvnsaoRgkM6v3Y",
        authDomain: "commentssection-ff702.firebaseapp.com",
        databaseURL: "https://commentssection-ff702-default-rtdb.firebaseio.com",
        projectId: "commentssection-ff702",
        storageBucket: "commentssection-ff702.appspot.com",
        messagingSenderId: "908377287279",
        };
        firebase.initializeApp(config);
        //Rootref is the whole database.
        const rootRef = firebase.database().ref();
        //commentsRef is defines the node where all the inputted comments will go
        const commentsRef = rootRef.child('comments');
        //Listen for click on Submit Comment button, and post comment.
        document.getElementById("btnSubmitComment").addEventListener("click", function () {
            //Replace line breaks in comment with br tags. ".value" is the text that was typed into the txcomment
            //when user presses enter/tab to break lines (create new paragraphs essentially) or add blank lines in the text they type, these will show in the box, but not on the page.
            //"/\n" (newline) "g" (global)is used to replace the new line characters and global signifies that it replaces all of them with the "<br>" tags
            var newcomment = document.getElementById('txComment').value.replace(/\n/g, "<br>");
            //Define a new, keyed post, this is a record/placholder in the database, each will have a unique key
            //commentsRef is the child database that is writing to, ".push" is a firebase commands, adds a new placholder for the data
            var newPostRef = commentsRef.push();
            //Fill tne new keyed post with data
            //all the below code is what get inputted into firebase
            newPostRef.set({
                name: document.getElementById('tbName').value.trim(),//".trim" simply removes any extra spaces
                comment: newcomment.trim(),//newcomment variable defined on line 20
                frompage: location.pathname,//path to specific page 
                when: firebase.database.ServerValue.TIMESTAMP//date and time on the server that data was sent at
            });
        });


           function showpastcomments() {
            var showat = document.getElementById('pastcomments');
            //Get comments whose from page equals this page's pathname.
            //access' the node "commentsref" in the databse, then access' the frompage stamp.
            //the "equalto" acts as a "filter" and essentially narrows down the specific data needed, in this case it'll be the location.pathname
            var commentsRef = firebase.database().ref('comments/').orderByChild('frompage').equalTo(location.pathname);
            //.once listens for exaclty one event of the specified event type, and then stops listening
            //here, the event type is "value", this event is used with the snapshot paramter, which reads a static snapshot a the commentsRef node
            commentsRef.once('value', function (snapshot) {
                //forEach guarantees that the children of the snapshot will be iterated in their correct order
                //this was needed as for each odbject (the individual comments), they have datestamps, therefore it is important that they are ordered correctly on the page 
                snapshot.forEach(function (itemSnapshot) {
                    //Get the object for one snapshot
                    var itemData = itemSnapshot.val();
                    var comment = itemData.comment;
                    var name = itemData.name;
                    var when = new Date(itemData.when).toLocaleDateString("en-us");
                    showat.innerHTML += "<li>" + comment + "<span> -- " + name + " (" + when +
                        ")</span></li>";
                })
            })
        }
        //Called when page first opens and also after Submit button click to show all comments for this page.
        showpastcomments()
