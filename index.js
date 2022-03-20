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
        .then(response => response.json()) // output json
}

function search(){
    const company = document.getElementById('company').value;
    const data2 = {
        company
    }    
    document.getElementById('message').innerHTML='Model training~~';
    postData('http://127.0.0.1:1000/scarpe',data2)
            .then(data2=>{
                const result = data2.return;
                const result2 = data2.return2;
                console.log(data2);
                console.log(result);
                console.log(result2);
                document.getElementById('good').value=result;
                document.getElementById('bad').value=result2;
                document.getElementById('message').innerHTML='Model training done';
            })
}

function submit(){
    const good = document.getElementById('good').value;
    const bad = document.getElementById('bad').value;
    const type = document.getElementById('type').value;
    const company = document.getElementById('company').value;

    
    const data={
        good,
        bad
    }

    if(company=='aapl'){
        
        if(type=='knn'){
            postData('http://127.0.0.1:1000/predict_KNN_AAPL',data)
            .then(data=>{
                const result = data.return;
                console.log(data);
                console.log(result);
                document.getElementById('resultText').innerHTML=result;
            })
        }else if((type=='rf')){
            postData('http://127.0.0.1:1000/predict_Rf_AAPL',data)
            .then(data=>{
                const result = data.return;
                console.log(data);
                console.log(result);
                document.getElementById('resultText').innerHTML=result;
            })
        }else if((type=='dt')){
            postData('http://127.0.0.1:1000/predict_Dt_AAPL',data)
            .then(data=>{
                const result = data.return;
                console.log(data);
                console.log(result);
                document.getElementById('resultText').innerHTML=result;
            })
        }else if((type=='svr')){
            postData('http://127.0.0.1:1000/predict_Svr_AAPL',data)
            .then(data=>{
                const result = data.return;
                console.log(data);
                console.log(result);
                document.getElementById('resultText').innerHTML=result;
            })
        }else if((type=='svc')){
            postData('http://127.0.0.1:1000/predict_Svc_AAPL',data)
            .then(data=>{
                const result = data.return;
                console.log(data);
                console.log(result);
                document.getElementById('resultText').innerHTML=result;
            })
        }
}else if(company=='mcd'){
        if(type=='knn'){
            postData('http://127.0.0.1:1000/predict_KNN_MCD',data)
            .then(data=>{
                const result = data.return;
                console.log(data);
                console.log(result);
                document.getElementById('resultText').innerHTML=result;
            })
        }else if((type=='rf')){
            postData('http://127.0.0.1:1000/predict_Rf_MCD',data)
            .then(data=>{
                const result = data.return;
                console.log(data);
                console.log(result);
                document.getElementById('resultText').innerHTML=result;
            })
        }else if((type=='dt')){
            postData('http://127.0.0.1:1000/predict_Dt_MCD',data)
            .then(data=>{
                const result = data.return;
                console.log(data);
                console.log(result);
                document.getElementById('resultText').innerHTML=result;
            })
        }else if((type=='svr')){
            postData('http://127.0.0.1:1000/predict_Svr_MCD',data)
            .then(data=>{
                const result = data.return;
                console.log(data);
                console.log(result);
                document.getElementById('resultText').innerHTML=result;
            })
        }else if((type=='svc')){
            postData('http://127.0.0.1:1000/predict_Svc_MCD',data)
            .then(data=>{
                const result = data.return;
                console.log(data);
                console.log(result);
                document.getElementById('resultText').innerHTML=result;
            })
        }
}
}