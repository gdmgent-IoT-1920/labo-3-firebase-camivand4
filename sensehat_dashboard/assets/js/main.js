const dbConfig = {
	collection: 'raspberry',
	document: 'lectorpi'
};

const app = {
	init() {
		// initialiseer de firebase app
		firebase.initializeApp(firebaseConfig);
		this._db = firebase.firestore();

		// cache the DOM
		this.cacheDOMElements();
		this.cacheDOMEvents();
	},
	cacheDOMElements() {

	},
	cacheDOMEvents() {

	},
	updateInFirebase() {

	}
}