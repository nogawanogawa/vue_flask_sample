import firebase from 'firebase'

const config = {
	apiKey: "AIzaSyDiK2ohwf8S3mz6qoXq7lmx9zBXcCZ2Ic8",
	authDomain: "fir-vue-398c1.firebaseapp.com",
	databaseURL: "https://fir-vue-398c1.firebaseio.com",
	projectId: "fir-vue-398c1",
	storageBucket: "fir-vue-398c1.appspot.com",
	messagingSenderId: "282617935",
};

const settings = { timestampsInSnapshots: true };
firebase.initializeApp(config);
firebase.firestore().settings(settings);

export default firebase