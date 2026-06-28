class TestSendPrintJobs:
    """Tests for HP Bridge send print jobs feature (picture and document)."""

    def test_send_picture_print_job(self):
        """
        Test that a picture print job can be sent and its UI is correct.
        Verifies the picture print flow from selection to job submission.
        """
        # TODO: Navigate to HP Bridge mini program home page (no method available)
        
        # Select picture print category
        self.fc.flow["print_flow"].select_picture_print()
        
        # Select from album
        self.fc.flow["print_flow"].select_from_album()
        
        # Pick a photo (using default index 0)
        self.fc.flow["print_flow"].pick_a_photo(index=0)
        
        # Verify print settings page is displayed correctly
        self.fc.flow["print_setting"].verify_print_setting_page()
        
        # Submit the print job
        self.fc.flow["print_setting"].select_print()
        
        # Verify job success submitted message
        self.fc.flow["print_setting"].verify_job_success_submitted_msg()


    def test_send_document_print_job_from_wechat(self):
        """
        Test that a document print job can be sent from WeChat.
        Verifies the document print flow from WeChat chat history to job submission.
        """
        # TODO: Navigate to HP Bridge mini program home page (no method available)
        # TODO: Ensure test document exists in WeChat chat history (setup required)
        
        # Select file print category
        self.fc.flow["print_flow"].select_file_print()
        
        # Verify selection options are displayed
        self.fc.flow["print_flow"].verify_select_options_exist(picture_print=False)
        
        # Select from chat history
        self.fc.flow["print_flow"].select_from_chat_history()
        
        # TODO: Need actual document file name from test data
        # Select specific document from chat history
        test_file_name = "test_document.pdf"  # TODO: Get from test data/fixture
        self.fc.flow["print_flow"].select_doc_from_chat_history(test_file_name)
        
        # Verify print settings page is displayed correctly
        self.fc.flow["print_setting"].verify_print_setting_page()
        
        # Verify the print job name matches the selected file
        self.fc.flow["print_setting"].verify_print_job_name(test_file_name)
        
        # Submit the print job
        self.fc.flow["print_setting"].select_print()
        
        # Verify job success submitted message
        self.fc.flow["print_setting"].verify_job_success_submitted_msg()
