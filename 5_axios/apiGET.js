import axios from "axios";

axios.get('http://localhost:8001/todos')
    .then(response => {
        console.log(response.data)
    })
