//
//  ViewController.swift
//  HospitalManagement
//
//  Created by Aiman Abdullah Anees on 23/01/17.
//  Copyright © 2017 Aiman Abdullah Anees. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var scrollView: UIScrollView!
    override func viewDidLoad() {
        super.viewDidLoad()
        
        var V1: PatientViewController = PatientViewController(nibName: "PatientViewController", bundle: nil) as! PatientViewController
        
        var V2: DoctorViewController = DoctorViewController(nibName: "DoctorViewController", bundle: nil) as! DoctorViewController
        
        
        self.addChildViewController(V1)
        self.scrollView.addSubview(V1.view)
        V1.didMove(toParentViewController: self)
        
        self.addChildViewController(V2)
        self.scrollView.addSubview(V2.view)
        V2.didMove(toParentViewController: self)
        
        
        //For Scrolling
        var V1Frame: CGRect = V1.view.frame
        V1Frame.origin.x = self.view.frame.width
        V1.view.frame=V1Frame
        
        
        self.scrollView.contentSize = CGSize(width: self.view.frame.width*2, height: self.view.frame.size.height)
        

    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
  
}

