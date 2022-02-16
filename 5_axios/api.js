const api = {
    key: "81b07fd757c71884477cb0d013b56d32",
    baseurl: "https://api.openweathermap.org/data/2.5",
};

const searchInput = document.querySelector(".search-input");
searchInput.addEventListener("keypress", setQuery);

// * enter Key 입력시 getResults 함수 실행
function setQuery(e) {
    if (e.keyCode == 13) { // keyCode는 키보드 입력값. 코드 13은 enter key에 해당됨.
        getResults(searchInput.value);
        //console.log(searchInput.value);
    }
}

// * API Call & displayResults function Call
function getResults(query) {
    // fetch(`${api.baseurl}/weather?q=${query}&APPID=${api.key}&units=metric`)
    //     .then((weather) => {
    //         return weather.json()
    //     })
    //     .then((weather) => displayResults(weather))
    //     .catch((err) => console.log("Error"));

    axios
        .get(`${api.baseurl}/weather?q=${query}&APPID=${api.key}&units=metric`)
        .then((weather) => displayResults(weather.data))
        .catch((err) => console.log(err));
}

// * class 선택 & innerText로 weather 주입
function displayResults(weather) {
    //console.log(weather);
    let city = document.querySelector(".location .city");
    city.innerText = `${weather.name}, ${weather.sys.country}`;

    let now = new Date();
    let date = document.querySelector(".location .date");
    date.innerText = dateBuilder(now);
    //console.log(now.getMonth());

    let temp = document.querySelector(".current .temp");
    temp.innerHTML = `${Math.round(weather.main.temp)} <span>°c<span>`;

    let weather_el = document.querySelector(".current .weather");
    weather_el.innerText = weather.weather[0].main;

    let hilow = document.querySelector(".current .hi-low");
    hilow.innerText = `${Math.round(weather.main.temp_min)} °c / ${Math.round(
        weather.main.temp_max
    )}°c`;
}

// * DateFormatter
function dateBuilder(d) {
    let months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ];
    let days = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ];

    let day = days[d.getDay()];
    let date = d.getDate();
    let month = months[d.getMonth()];
    let year = d.getFullYear();

    return `${day} ${date} ${month} ${year}`;
}
