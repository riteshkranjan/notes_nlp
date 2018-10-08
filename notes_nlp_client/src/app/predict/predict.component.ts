import { Component, OnInit } from '@angular/core';
import { AppService } from '../../app.service';
import { ServiceResponse } from '../../service.response.interface';

@Component({
  selector: 'app-predict',
  templateUrl: './predict.component.html',
  styleUrls: ['./predict.component.css']
})
export class PredictComponent implements OnInit {

  isRequesting:boolean = false;
  response:ServiceResponse = {debugInfo:'', predictions:[]};
  search:string = '';
  constructor(private appService: AppService) { }

  ngOnInit() {
  }

  getResults(){  
    this.isRequesting = true;  
    this.response = {debugInfo:'', predictions:[]};
    this.appService.getResponseForPredict(this.search).subscribe((response) => 
        {          
          this.response = response;
          this.isRequesting = false;
        }
    );
   
  }

  reset(){
    this.search='';
    this.response = {debugInfo:'', predictions:[]};
  }

}
