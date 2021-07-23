var pdbFile = null;
const darkModIndicator = document.getElementById('darkIndicator');

const btnGenerateFASTA = document.getElementById('btnGenerateFASTA');
const btnOpenGraphic = document.getElementById('btnOpenGraphic');
const btnExecFoldX = document.getElementById('btnExecFoldX');

window.lynxCBRV = {
    checkPDB: async () => {
      div = document.getElementById("pdbNotify");
      if(pdbFile == null){
        div.innerHTML=`
        <div class="info-box warning col-12" style="position:relative;">
          <div class="info-box-content">
            Remember, it is necessary to select a PDB file in order to verify it.
          </div>
        </div>
        `
      }else{
        let com = 'python3 resources/scripts/verify.py '.concat(pdbFile);
        let response = await Neutralino.os.execCommand({
          command: com
        });
        let resp = JSON.parse(response.output);
        if (resp.code == 200) {
          btnGenerateFASTA.disabled = false;
          btnExecFoldX.disabled = false;
          div.innerHTML=`
          <div class="info-box success col-12" style="position:relative;">
            <div class="info-box-content">
              `.concat(resp.response).concat(`
            </div>
          </div>
          `)
        }else{
          div.innerHTML=`
          <div class="info-box alert col-12" style="position:relative;">
            <div class="info-box-content">
              `.concat(resp.response).concat(`
            </div>
          </div>
          `)
        }
      }
    },
    openPDB: async () => {
      let response = await Neutralino.os.showDialogOpen({
        title: 'Select Your PDB'
      });
      pdbFile = response.selectedEntry;
      setPathInfo();
    },
    execFoldX : async () =>{
      Metro.dialog.open("#foldxDialog");
      let com = 'python3 resources/scripts/foldx.py';
      await Neutralino.os.execCommand({
        command: com
      });
      let com2 = 'python3 resources/scripts/parse_foldx.py'
      let response = await Neutralino.os.execCommand({
        command: com2
      });
      var list = JSON.parse(response.output.replace(/'/g, '"'));
      console.log(list);
      div = document.getElementById("tableFoldx");
      var html = `
      <div class="container transparent-style">
      <table class="table text-center">
        <thead>
          <tr>
            <th class="text-center">Atom</th>
            <th class="text-center">Number</th>
            <th class="text-center">Binding Energy (kJ/mol)</th>
          </tr>
        </thead>
        <tbody>
      `
      for (let elem of list){
        console.log(elem);
        console.log(elem.atom);
        html = html.concat(`
          <tr>
            <td>
          `).concat(elem.atom).concat(`
            </td><td>
          `).concat(elem.number).concat(`
            </td><td>
          `).concat(elem.energy).concat(`
            </td>
          </tr>
          `)
      }
      html = html.concat(`
        </tbody>
      </table>
      </div>
      `);
      div.innerHTML = html;
      btnOpenInPyMol.disabled = false;
      Metro.dialog.close("#foldxDialog");
    },
    openInPyMol : async () =>{
      let com = 'python3 resources/scripts/openPymol.py '.concat(getColor()).concat(" ").concat(getAmstroms()).concat(" ").concat(pdbFile);
      console.log(com);
      let response = await Neutralino.os.execCommand({
        command: com
      });
    },
    clear : async () =>{
      btnGenerateFASTA.disabled = true;
      btnExecFoldX.disabled = true;
      btnOpenInPyMol.disabled = true;
      btnOpenGraphic.disabled = true;
      btnShowAlignment.disabled = true;
      await Neutralino.os.execCommand({
        command: 'python3 resources/scripts/clear.py'
      });
      div = document.getElementById("tableFoldx");
      div.innerHTML = "";
      div = document.getElementById("alignDiv");
      div.innerHTML = "";
      div = document.getElementById("pdbNotify");
      div.innerHTML = "";
      pdbFile = null;
      setPathInfo();
    },
    showAlignment: async () => {
      div = document.getElementById("alignDiv");
      let response = await Neutralino.os.execCommand({
        command: 'python3 resources/scripts/alignments.py'
      });
      div.innerHTML = `
        <div class="container transparent-style">
          <div class="embed-container">
            <iframe src="../temp/align.html" allowfullscreen></iframe>
          </div>
        </div>
      `
    },
    generateFasta: async () => {
      Metro.dialog.open("#fastaDialog");
      let com = 'python3 resources/scripts/getSecuencia.py '.concat(pdbFile);
      let response = await Neutralino.os.execCommand({
        command: com
      });
      btnShowAlignment.disabled = false;
      btnOpenGraphic.disabled = false;
      Metro.dialog.close("#fastaDialog");
    },
    graficarFasta : async () =>{
      Metro.dialog.open("#graphicDialog");
      await Neutralino.os.execCommand({
        command: 'python3 resources/scripts/graficarFasta.py'
      });
      Metro.dialog.close("#graphicDialog");
    },
    installReq : async () =>{
      Metro.dialog.open("#depDialog");
      await Neutralino.os.execCommand({
        command: 'pip3 install -r requisitos'
      });
      Metro.dialog.close("#depDialog");
    }
};

// Funciones

function setPathInfo(){
  div = document.getElementById("divFilePath");
  if (pdbFile) {
    div.value = pdbFile;
  }else{
    div.value = `You didn't select any file`;
    btnGenerateFASTA.disabled = true;
    btnOpenGraphic.disabled = true;
  }
}

function getColor(){
  div = document.getElementById("selectColor");
  return div.value
}

function getAmstroms(){
  div = document.getElementById("inputAmstom");
  return div.value
}

function toggleDarkMode(){
  if (darkIndicator.checked) {
    document.documentElement.style.setProperty('--bg-color', 'rgba(0,0,0,0.85)');
    document.documentElement.style.setProperty('--font-color', '#FFF');
  }else {
    document.documentElement.style.setProperty('--bg-color', 'rgba(255,255,255,0.85)');
    document.documentElement.style.setProperty('--font-color', '#000');
  }
}

function changePrimaryColor(color){
  document.documentElement.style.setProperty('--primary-color', String(color));
}

// Secuencia de inicio
Neutralino.init();
setPathInfo();
window.lynxCBRV.clear();
