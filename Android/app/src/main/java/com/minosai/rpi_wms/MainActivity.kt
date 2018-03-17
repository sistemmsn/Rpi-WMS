package com.minosai.rpi_wms

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.Window
import android.widget.Toast
import com.google.firebase.database.*
import kotlinx.android.synthetic.main.activity_main.*
import java.text.SimpleDateFormat
import java.util.*

class MainActivity : AppCompatActivity() {

    var stateCounter = 0

    class Data() {
        var humidity: String = ""
        var pressure: String = ""
        var temperature: String = ""
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        supportActionBar!!.hide()

        var database: FirebaseDatabase = FirebaseDatabase.getInstance()
        var dataRef: DatabaseReference = database.getReference("data")

        val listener = object : ValueEventListener {
            override fun onCancelled(p0: DatabaseError?) {
            }

            override fun onDataChange(dataSnapshot: DataSnapshot?) {
                var data: Data = dataSnapshot!!.getValue<Data>(Data::class.java)!!
                text_temprature.text = "${data.temperature}°C"
                text_pressure.text = data.pressure
                text_humidity.text = "${data.humidity}%"
            }
        }

        dataRef.addValueEventListener(listener)

        text_date_time.text = "${SimpleDateFormat("EEEE").format(Date())} | ${Date().date} ${SimpleDateFormat("MMMM").format(Date())}"
    }
}
