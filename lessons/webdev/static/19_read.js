Vue.createApp({
    data() {
        return {
            users: []
        }
    },
    async mounted() {
        const response = await fetch('/api/users');
        this.users = await response.json();
    }
}).mount('body');