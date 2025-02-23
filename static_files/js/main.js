async function FillMyInfo(){
    try{
        let response = await fetch('http://127.0.0.1:3001/api/')
        
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        const json = await response.json()
        window.location = json.data
    }    
    catch(e){
        console.log(e.message)
    }
};

async function sendMyInfoCallback(auth_code){
    try{
        let response = await fetch('http://127.0.0.1:3001/api/sendmyinfo/', {
            method: 'POST',
            headers: {
                'Accept': 'application/json, text/plain, */*',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                'auth_code': auth_code
            })
        });

        const content = await response.json()
        return content;

    }catch(e){
        console.log(e.message)
    }
}

function InjectHTML(){
    
}