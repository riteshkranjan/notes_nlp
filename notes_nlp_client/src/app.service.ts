import { Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { ServiceResponse } from './service.response.interface';


import { Observable } from 'rxjs/Rx';
import { BehaviorSubject } from 'rxjs/Rx'; 

// Add the RxJS Observable operators we need in this app.
import './rxjx-operators';
import { error } from 'selenium-webdriver';


@Injectable()

export class AppService {
  baseUrl: string = '';
  responses: ServiceResponse[] = [];
  constructor(private http: Http, private httpClient: HttpClient) {   
    this.baseUrl = '/api';
    this.responses.push({debugInfo: 'Debug Info Received From NLP Service', predictions: [
        {name:"Priority 1", percentage: 90, priority: 1}       
    ]});


    this.responses.push({debugInfo: '', predictions: [
        {name:"Priority 1", percentage: 90, priority: 1},
        {name:"Priority 2", percentage: 7, priority: 2},
        {name:"Priority 3", percentage: 3, priority: 3},
        {name:"Priority 4", percentage: 0, priority: 4},
        {name:"Priority 5", percentage: 0, priority: 5}
    ]});
  }

  getResponseForPredict(search: string): Observable<ServiceResponse> {   
        let headers = new Headers({ 'Content-Type': 'application/json' });
        let options = new RequestOptions({ headers: headers });
        let apiURL = 'http://localhost:5001/predict/'+search;
        return this.http.get(apiURL, { headers })
        .map((response: Response) => {              
        return <ServiceResponse>response.json();
        })
        .catch((error: any) => {           
        return Observable.throw(new Error(error.status));            
        });    
          //return Observable.of(this.responses[1]).delay(2000);
  }

  getResponseForNLP(search: string): Observable<ServiceResponse> {      
    let headers = new Headers({ 'Content-Type': 'application/json' });
    let options = new RequestOptions({ headers: headers });
    let apiURL = 'http://localhost:5001/process_nlp';// + search;
    let data = {"data":search};
    return this.http.post(apiURL, search, { headers })
          .map((response: Response) => {              
              return <ServiceResponse>response.json();
          })
          .catch((error: any) => {           
                return Observable.throw(new Error(error.status));            
        });   
        //return Observable.of(this.responses[0]).delay(2000);; 
  }


  
}

