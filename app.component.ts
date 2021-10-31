import { Component } from '@angular/core';
import{HttpClient} from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'TASKPVP';
  name: String;
  Data= {}

  constructor(private http:HttpClient){}
  ngOnInit()
  {
	  this.http.get('https://flaskpvp11.herokuapp.com/opinion')
	  .subscribe((data)=>{
      this.Data = data;
		  console.warn(this.Data);
      
      
	  })
  }
  onSubmit(dataPost){
      console.warn(dataPost)
      this.http.post("https://flaskpvp11.herokuapp.com/opinion",dataPost)
      .subscribe((data)=>{
      this.Data =data;  
      console.warn(data)})
    }


  }





