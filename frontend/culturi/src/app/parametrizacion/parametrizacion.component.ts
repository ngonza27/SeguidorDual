import { Component, OnInit } from '@angular/core';
import {ApiConenctionService} from '../api-conenction.service'
import { interval } from 'rxjs'

@Component({
  selector: 'app-parametrizacion',
  templateUrl: './parametrizacion.component.html',
  styleUrls: ['./parametrizacion.component.css']
})
export class ParametrizacionComponent implements OnInit {

  constructor(private apiConnection:ApiConenctionService) { }

  history = null

  ngOnInit() {
    this.apiConnection.getAllLiveData().subscribe(res=>{
      const base = res['body']
      var history = document.getElementById('history');
      for (var i = 0; i < base.length; i++) {
        var tr = "<tr>";
        tr += "<th>" + base[i].solar_panel_data.temperatura + "</th>" 
            + "<th>" + base[i].solar_panel_data.posicionX + "</th>"
            + "<th>" + base[i].solar_panel_data.posicionZ + "</th>"
            + "<th>" + base[i].solar_panel_data.voltaje + "</th>" 
            + "<th>" + base[i].solar_panel_data.corriente + "</th>" 
            + "</tr>";
            //TODO: AGREGAR CODIGO CSS <style>....</style>
        history.innerHTML += tr;
      }
      console.log(base)
      this.history=base
    })
    setTimeout(
      function(){ 
      location.reload(); 
      }, 50000);
  }
}
