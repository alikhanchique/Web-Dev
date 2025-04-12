import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CompanyService } from '../../services/company.service';
import { Vacancy } from '../../models/vacancy';

@Component({
  selector: 'app-company-detail',
  templateUrl: './company-detail.component.html',
})
export class CompanyDetailComponent implements OnInit {
  vacancies: Vacancy[] = [];

  constructor(
    private route: ActivatedRoute,
    private companyService: CompanyService
  ) {}

  ngOnInit(): void {
    const companyId = Number(this.route.snapshot.paramMap.get('id'));
    this.companyService.getCompanyVacancies(companyId).subscribe(data => {
      this.vacancies = data;
    });
  }
}
