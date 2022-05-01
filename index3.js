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
    document.getElementById('his').innerHTML="<a href='javascript:show_"+company+"_his()'>See Past Year History Prices</a>";
    
    const today = new Date();

    const open_date = today.getFullYear()+'/'+(today.getMonth()+1)+'/'+(today.getDate()-7);
    const end_date = today.getFullYear()+'/'+(today.getMonth()+1)+'/'+today.getDate();

    document.getElementById('today').innerHTML=""+open_date+" to "+end_date+"";
    const data2 = {
        company
    }    
    document.getElementById('message').innerHTML='Data are scraping from Twitter~~';
    postData('http://127.0.0.1:1000/scarpe_more',data2)
            .then(data2=>{
                const result = data2.return;
                const result2 = data2.return2;
                const result3 = data2.return3;
                const result4 = data2.return4;
                console.log(data2);
                console.log(result);
                console.log(result2);
                console.log(result3);
                console.log(result4);
                document.getElementById('good').value=result;
                document.getElementById('bad').value=result2;
                document.getElementById('close').value=result3;
                document.getElementById('vol').value=result4;
                document.getElementById('message').innerHTML='Data scraping done';
                document.getElementById('img2').innerHTML="<a href='javascript:show_img2()'>Show some Tweets</a>";
            })
}

function submit(){
    const good = document.getElementById('good').value;
    const bad = document.getElementById('bad').value;
    const close = document.getElementById('close').value;
    const vol = document.getElementById('vol').value;
    const type = document.getElementById('type').value;
    const company = document.getElementById('company').value;

    
    const data={
        good,
        bad,
        close,
        vol
    }

    if(company=='aapl'){
        
        if(type=='lg'){
            postData('http://127.0.0.1:1000/predict_Lg_AAPL_more',data)
            .then(data=>{
                const result = data.return;
                const r2 = data.r2;
                console.log(data);
                console.log(result);
                document.getElementById('resultText').innerHTML=result;
                document.getElementById('r2').innerHTML=r2;
                document.getElementById('img').innerHTML="<a href='javascript:show_AAPL_lg()'>Show the graph of model</a>";
            })
        }
        
}else if(company=='mcd'){
        if(type=='lg'){
            postData('http://127.0.0.1:1000/predict_Lg_MCD_more',data)
            .then(data=>{
                const result = data.return;
                const r2 = data.r2;
                console.log(data);
                console.log(result);
                document.getElementById('resultText').innerHTML=result;
                document.getElementById('r2').innerHTML=r2;
                document.getElementById('img').innerHTML="<a href='javascript:show_MCD_lg()'>Show the graph of model</a>";
            })
        }
        }

}