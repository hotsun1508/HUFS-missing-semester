import axios from "axios";

axios({
    url: 'http://localhost:8001/todos',
    method: 'GET',
})
    .then(response => {
        console.log(response.data)
    })
    .catch((err) => console.log(err));
