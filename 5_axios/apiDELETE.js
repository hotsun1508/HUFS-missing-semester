import axios from "axios";

axios.delete('http://localhost:8001/todos/5')
    .then((response) => {
        console.log(response.data)
    })
    .catch((error) => {
        console.log(error)
    })