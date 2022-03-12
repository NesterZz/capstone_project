function postData(url, data) {
    // Default options are marked with *
    return fetch(url, {
        body: JSON.stringify(data), // must match 'Content-Type' header
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, same-origin, *omit
        headers: {
            'user-agent': 'Example',
            'content-type': 'application/json'
        },
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, cors, *same-origin
        redirect: 'follow', // manual, *follow, error
        referrer: 'no-referrer', // *client, no-referrer
    })
        .then(response => response.json()) // 輸出成 json
}

function submit(){
    const good = document.getElementById('good').value;
    const bad = document.getElementById('bad').value;
    const type = document.getElementById('type').value;

    const data = {
        good,
        bad
    }
    if(type=='knn'){
        postData('http://192.168.0.112:1000/predict_KNN',data)
        .then(data=>{
            const result = data.return;
            console.log(data);
            console.log(result);
            document.getElementById('resultText').innerHTML=result;
        })
    }else if((type=='rf')){
        postData('http://192.168.0.112:1000/predict_Rf',data)
        .then(data=>{
            const result = data.return;
            console.log(data);
            console.log(result);
            document.getElementById('resultText').innerHTML=result;
        })
    }else if((type=='dt')){
        postData('http://192.168.0.112:1000/predict_Dt',data)
        .then(data=>{
            const result = data.return;
            console.log(data);
            console.log(result);
            document.getElementById('resultText').innerHTML=result;
        })
    }else if((type=='svr')){
        postData('http://192.168.0.112:1000/predict_Svr',data)
        .then(data=>{
            const result = data.return;
            console.log(data);
            console.log(result);
            document.getElementById('resultText').innerHTML=result;
        })
    }else if((type=='svc')){
        postData('http://192.168.0.112:1000/predict_Svc',data)
        .then(data=>{
            const result = data.return;
            console.log(data);
            console.log(result);
            document.getElementById('resultText').innerHTML=result;
        })
    }
}