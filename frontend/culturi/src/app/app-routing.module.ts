import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {HomeComponent}from '../app/home/home.component';
import {ParametrizacionComponent}from '../app/parametrizacion/parametrizacion.component'

const routes: Routes = [
  {path:'',redirectTo:'home', pathMatch: 'full' },
  {path:'home',component:HomeComponent},
  {path:'parametrizacion',component:ParametrizacionComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes, { relativeLinkResolution: 'legacy' })],
  exports: [RouterModule]
})
export class AppRoutingModule { }
