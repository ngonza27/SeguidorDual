import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiConenctionService {

  constructor(private httClient: HttpClient) { }

  getLiveData() {
    return this.httClient.get("https://01sttl2a6l.execute-api.us-east-2.amazonaws.com/test/")
  }

  getAllLiveData() { 
    return this.httClient.get("https://01sttl2a6l.execute-api.us-east-2.amazonaws.com/test/getall")
  }

}
