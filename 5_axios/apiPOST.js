import axios from "axios";

const postData = {
    "id": 5,
    "content": "R",
    "completed": false
};

axios({
    url: 'http://localhost:8001/todos',
    method: 'POST',
    data: postData
})
    .then(response => {
        console.log(response.data)
    })
    .catch((err) => console.log(err));