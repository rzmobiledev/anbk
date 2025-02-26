
async function getMyInfoUrl(){
    try{
        let response = await fetch('http://127.0.0.1:3001/api/myinfo/');
        
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

async function sendMyInfoPayload(auth_code){
    try{
        let response = await fetch('http://127.0.0.1:3001/api/myinfo/', {
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
        return content

    }catch(e){
        console.log(e.message)
    }
}

function updateDomElement(data){
      
      const employment = filteringPIVal(data['employmentsector'])
      InjectHTML('Employment Sector', employment, "collapse1")

      const uinfin = filteringPIVal(data['uinfin'])
      InjectHTML('UINFIN', uinfin, "collapse2")

      const name = filteringPIVal(data['name'])
      InjectHTML('Full Name', name, "collapse3")

      const sex = filteringPIDesc(data['sex'])
      InjectHTML('Sex', sex, "collapse4")

      const race = filteringPIDesc(data['race'])
      InjectHTML('Race', race, "collapse5")

      const dob = filteringPIVal(data['dob'])
      InjectHTML('Date Of Birth', dob, "collapse6")

      const resident = filteringPIDesc(data['residentialstatus'])
      InjectHTML('Residential Status', resident, "collapse7")

      const nationality = filteringPIDesc(data['nationality'])
      InjectHTML('Nationality', nationality, "collapse8")

      const birthcountry = filteringPIDesc(data['birthcountry'])
      InjectHTML('Birth Country', birthcountry, "collapse9")

      const passtype = filteringPIDesc(data['passtype'])
      InjectHTML('Pass Type', passtype, "collapse10")

      const passstatus = filteringPIDesc(data['passstatus'])
      InjectHTML('Pass Status', passstatus, "collapse11")

      const passexpirydate = filteringPIVal(data['passexpirydate'])
      InjectHTML('Pass Expiry Date', passexpirydate, "collapse12")

      const mobile = filteringMobile(data['mobileno'])
      InjectHTML('Mobile Number', mobile, 'collapse13')

      const email = filteringPIVal(data['email'])
      InjectHTML('Email', email, "collapse14")

      const regadd = filteringRegadd(data['regadd'])
      InjectHTML('Registered Address', regadd, 'collapse15')

      const housingtype = filteringPIDesc(data['housingtype'])
      InjectHTML('Housing Type', housingtype, "collapse16")

      const marital = filteringPIDesc(data['marital'])
      InjectHTML('Marital Status', marital, "collapse17")

  
}

function filteringPIVal(data){
  return `
        Last Updated : <b>${data['lastupdated']}</b><br/>
        Source: <b>${data['source']}</b><br/>
        classification: <b>${data['classification']}</b><br/>
        Value: <b>${data['value']}</b>
      `
}

function filteringPIDesc(data){
  return `
        Last Updated : <b>${data['lastupdated']}</b><br/>
        Code : <b>${data['code']}</b><br/>
        Source: <b>${data['source']}</b><br/>
        classification: <b>${data['classification']}</b><br/>
        Desc: <b>${data['desc']}</b>
      `
}

function filteringMobile(data){
  return `
    Last Updated : <b>${data['lastupdated']}</b><br/>
    Source: <b>${data['source']}</b><br/>
    classification: <b>${data['classification']}</b><br/>
    Mobile: <b>${data['prefix']['value']}${data['areacode']['value']}${data['nbr']['value']}</b>
  `
}

function filteringRegadd(data){
  return `
    Country: <b>${data['country']['desc']}</b><br/>
    Unit: <b>${data['unit']['value']}</b><br/>
    Street: <b>${data['street']['value']}</b><br/>
    Block: <b>${data['block']['value']}</b><br/>
    Source: <b>${data['source']}</b><br/>
    Postal: <b>${data['postal']['value']}</b><br/>
    Classification: <b>${data['classification']}</b><br/>
    Floor: <b>${data['floor']['value']}</b><br/>
    Type: <b>${data['type']}</b><br/>
    Building: <b>${data['building']['value']}</b>
  `
}

function InjectHTML(title, val, idCollapse){
    
    const container = document.getElementById('accordionExample')
    const div = document.createElement('div')
    div.className = "accordion-item"
    const h2 = document.createElement('h2')
    h2.className = "accordion-header"

    const button = document.createElement('button')
    button.type = "button"
    button.classList = "accordion-button collapsed"
    button.dataset.bsTarget = `#${idCollapse}`
    button.dataset.bsToggle = "collapse"
    button.ariaExpanded = "true"
    button.setAttribute('aria-controls', idCollapse)
    button.textContent = title
    
    h2.appendChild(button)
    div.appendChild(h2)
    container.appendChild(div)

    const div2 = document.createElement('div')
    div2.id = idCollapse
    div2.classList = "accordion-collapse collapse"
    div2.dataset.bsParent = "#accordionExample"

    const div3 = document.createElement('div')
    div3.classList = "accordion-body"
    div3.innerHTML = val

    div2.appendChild(div3)
    div.appendChild(div2)
}