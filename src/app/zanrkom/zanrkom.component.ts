import { Component } from '@angular/core';
import { ApiService } from '../api.service';
import { MatDialog } from '@angular/material/dialog';
import { DialogComponent } from '../dialog/dialog.component';

@Component({
  selector: 'app-zanrkom',
  templateUrl: './zanrkom.component.html',
  styleUrls: ['./zanrkom.component.scss']
})
export class ZanrkomComponent {
  knjigas = [{ naziv: 'Test' }];
  selectedBook;
  constructor(private api: ApiService, public dialog: MatDialog) {
    this.getKnjigas();
    this.selectedBook = {
      id: -1, autor: '', broj_primeraka: '', broj_strana: '', godina_izdanja: '', izdavac: '', naziv: '', pismo: '', vrsta_poveza: '', zanr: '', img: ''
    };
  }

  getKnjigas = () => {
    this.api.getKnjigasZanrKom().subscribe(
      data => {
        this.knjigas = data;
      },
      error => {
        console.log(error);
      }
    );
  }
  knjigaClicked = (knjiga) => {
    this.api.getOneKnjiga(knjiga.id).subscribe(
      data => {
        this.selectedBook = data;
        localStorage.setItem('id', data.id);
        localStorage.setItem('naziv', data.naziv);
        localStorage.setItem('autor', data.autor);
        localStorage.setItem('izdavac', data.izdavac);
        localStorage.setItem('broj_strana', data.broj_strana);
        localStorage.setItem('godina_izdanja', data.godina_izdanja);
        localStorage.setItem('vrsta_poveza', data.vrsta_poveza);
        localStorage.setItem('pismo', data.pismo);
        localStorage.setItem('zanr', data.zanr);
        localStorage.setItem('img', data.img);
      },
      error => {
        console.log(error);
      }
    );
  }

  openDialog(knjiga) {
    this.knjigaClicked(knjiga);
    this.dialog.open(DialogComponent);
  }
}
