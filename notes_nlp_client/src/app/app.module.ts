import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { HttpClientModule } from '@angular/common/http'; 
import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app.routing.module'
import { AppComponent } from './app.component';
import { AppService } from '../app.service';
import { PredictComponent } from './predict/predict.component';
import { NavMenuComponent } from './navmenu/navmenu.component';
import { HomeComponent } from './home/home.component';
import { NotesComponent } from './notes/notes.component';
import {SpinnerComponent} from '../spinner/spinner.component'; 

@NgModule({
  declarations: [
    AppComponent,
    PredictComponent,
    NotesComponent,
    NavMenuComponent,
    HomeComponent,
    SpinnerComponent
, NotesComponent  ],
  imports: [
    HttpModule,
    HttpClientModule,
    BrowserModule,
    AppRoutingModule,
    FormsModule
  ],
  exports: [SpinnerComponent],
  providers: [AppService],
  bootstrap: [AppComponent]
})
export class AppModule { }
