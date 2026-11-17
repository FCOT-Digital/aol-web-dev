Vue.createApp({
    data() {
        return {
            given_name: '',
            email: '',
            message: '',
        }
    },
    methods: {
        async submitForm() {
            this.message = 'Sending request...'
            const response = await fetch('/api/users', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    given_name: this.given_name,
                    email: this.email
                })
            })
            const data = await response.json()
            this.message = data.message
        }
    }
}).mount('body')
