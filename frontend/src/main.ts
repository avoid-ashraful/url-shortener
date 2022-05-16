import { createApp } from 'vue'
import App from './App.vue'

import PrimeVue from "primevue/config";
import InputText from 'primevue/inputtext';






import "primevue/resources/themes/saga-blue/theme.css"; //theme
import "primevue/resources/primevue.min.css"; //core css
import "primeicons/primeicons.css"; //icons




createApp(App)
    .use(PrimeVue)
    .component("InputText", InputText)

    .mount('#app')