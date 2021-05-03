import { Component, OnInit } from '@angular/core';
import {ApiConenctionService} from '../api-conenction.service'
import { interval } from 'rxjs'

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor(private apiConnection:ApiConenctionService) { }

    gaugeType = "semi";
    gaugeValue = 20;
    gaugeAppendText = "°C";
    voltaje=10
    corriente=0.5
    posicionX=23
    posicionZ=5

  ngOnInit() {
    const emitter = interval(3000);
    emitter.subscribe(data=>{
      this.apiConnection.getLiveData().subscribe(res=>{

        const base = res['body']['solar_panel_data']
        console.log(base)
        this.gaugeValue=base['temperatura']
        this.voltaje=base["voltaje"]
        this.corriente=base["corriente"]
        this.posicionX=base["posicionX"]
        this.posicionZ=base["posicionZ"]
      })
    })
  }
}
