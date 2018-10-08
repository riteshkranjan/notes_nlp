import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {PredictComponent} from './predict/predict.component';
import {NotesComponent} from './notes/notes.component';
import { NavMenuComponent } from './navmenu/navmenu.component';
import { HomeComponent } from './home/home.component';


const routes: Routes = [
{ path: 'predict', component: PredictComponent },
{ path: 'notes', component: NotesComponent },
{ path: 'home', component: HomeComponent },
{path : '', component : PredictComponent}
];

@NgModule({
imports: [
RouterModule.forRoot(routes)
],
exports: [
RouterModule
],
declarations: []
})
export class AppRoutingModule { }