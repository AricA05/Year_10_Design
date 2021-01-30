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
            //Replace line breaks in comment with br tags.
            var newcomment = document.getElementById('txComment').value.replace(/\n/g, "<br>");
            //Define a new, keyed post.
            var newPostRef = commentsRef.push();
            //Fill tne new keyed post with data
            //all the below code is what get inputted into firebase
            newPostRef.set({
                name: document.getElementById('tbName').value.trim(),
                comment: newcomment.trim(),
                frompage: location.pathname,
                when: firebase.database.ServerValue.TIMESTAMP
            });
        });
