Vue.createApp({
    data() {
        return {
            greeting: '',
            name: ''
        }
    },
    methods: {
        sayHello() {
            this.greeting = `Hello ${this.name}, from Vue!`;
        }
    }
}).mount('#app');